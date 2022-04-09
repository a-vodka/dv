import numpy as np

supported_modifiers = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}


def get_von_Mises_stress(data):
    S11, S12, S13 = data[0, :]
    _, S22, S23 = data[1, :]
    _, _, S33 = data[2, :]
    stress_1 = ((S11 - S22) ** 2 + (S22 - S33) ** 2 + (S11 - S33) ** 2)
    stress_2 = 6 * (S12 ** 2 + S13 ** 2 + S23 ** 2)
    stress = np.sqrt((stress_1 + stress_2) / 2)
    return stress


def get_tensor_diagonalization_data(tensor):
    eigvals, eigvecs = np.linalg.eigh(tensor)
    origin_vectors = np.array([[1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    angles = []
    indices = np.argsort(eigvals)[::-1]
    eigvals = eigvals[indices]
    eigvecs = eigvecs[:, indices]

    for axis in range(len(eigvals)):
        vector = eigvecs[:, axis]
        basis = origin_vectors[:, axis]
        angle_cos = np.dot(vector, basis) / np.linalg.norm(vector) / np.linalg.norm(basis)
        angles.append(np.arccos(angle_cos))
    angles = np.array(angles)
    return eigvals, angles


def Rx(theta):
    return np.matrix([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])


def Ry(theta):
    return np.matrix([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])


def Rz(theta):
    return np.matrix([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])


def rotate_glyph_surface(glyph_data, angles):
    Rotation_operators = [Rx, Ry, Rz]
    rotated_data = glyph_data
    for axis in range(len(angles)):
        R = Rotation_operators[axis](angles[axis])
        rotated_data = np.einsum('ji, mni -> jmn', R, np.dstack(rotated_data))
    return rotated_data


def get_glyph_data(position, tensor, limits_data, glyph_radius=1.0, glyph_points=12, superquadrics_option=0,
                   glyph_type=0):
    """
    glyph_type = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}

    if glyph_type == 3 (superquadric)
    there are glyph shape type
    0 - superquadrics,
    1 - Kindlmann_glyph,
    2 - Kindlmann_modified_glyph

    """
    surface_functions = [Superquadrics, Kindlmann_glyph, Kindlmann_modified_glyph]

    lambdas, angles = get_tensor_diagonalization_data(tensor)
    # radiuses = np.interp(lambdas, [min(lambdas), max(lambdas)], (0.5*glyph_radius, 1.5*glyph_radius))
    # [Cl, Cs, Cp] = np.interp(lambdas, limits_data, (1.4, 5))  # classical superellipse
    [Cl, Cs, Cp] = lambdas  # by Ennis
    u_border = np.pi
    u_step = u_border / glyph_points
    v_border = np.pi / 2
    v_step = v_border / glyph_points
    u = np.arange(-u_border - u_step, u_border + u_step, u_step)
    v = np.arange(-v_border - v_step, v_border + v_step, v_step)
    u, v = np.meshgrid(u, v)
    surf_fun = surface_functions[superquadrics_option]
    # # surf_fun = Superquadrics
    # surf_fun = Kindlmann_modified_glyph
    # # surf_fun = Kindlmann_glyph
    # X, Y, Z = superellipse((u, v), (Cl, Cs, Cp), glyph_radius)  # classical superellipse
    # X, Y, Z = Kindlmann_glyph((u, v), (Cl, Cs, Cp), radiuses)  # by Ennis
    X, Y, Z = surf_fun((u, v), lambdas, glyph_radius, limits_data, shape=supported_modifiers[glyph_type],
                       radius_scaling=True)
    X, Y, Z = rotate_glyph_surface((X, Y, Z), angles)
    X += position[0]
    Y += position[1]
    Z += position[2]
    return X, Y, Z


def get_color(tensor, limits_data):
    Stress = get_von_Mises_stress(tensor)
    red = np.interp(Stress, limits_data, (0, 1))
    RGB = red, 0, 1 - red
    return RGB


def get_colormap_ratio(tensor, limits_data):
    Stress = get_von_Mises_stress(tensor)
    # ratio = 1 - np.interp(Stress, limits_data, (0.25, 1))
    ratio = np.interp(Stress, limits_data, (0, 1))
    return ratio


def get_colormap_ratio_on_stress(stress, limits_data):
    ratio = np.interp(stress, limits_data, (0, 1))
    return ratio


def sn(w, m): return np.sign(np.sin(w)) * np.abs(np.sin(w)) ** m


def cs(w, m): return np.sign(np.cos(w)) * np.abs(np.cos(w)) ** m


def Superquadrics(coordinates, lambdas, radius, scale_data, shape='cuboid', concavity=True, radius_scaling=True):
    u, v = coordinates
    if shape == supported_modifiers[0]:
        r, s, t = 10, 10, 10
    elif shape == supported_modifiers[1]:
        r, s, t = 10, 2, 2
    elif shape == supported_modifiers[2]:
        r, s, t = 2, 2, 2
    elif shape == supported_modifiers[3]:
        max_degree = 3 if concavity else 4
        min_degree = -1 if concavity else 0
        # r, s, t = lambdas
        # Cl = (r-s)/sum(lambdas)
        # Cp = 2*(s-t)/sum(lambdas)
        # Cs = 3*t/sum(lambdas)
        degrees = np.interp(lambdas, scale_data, (-min_degree, max_degree))
        r, s, t = np.power(2, degrees)
        # r, s, t = Cl, Cp, Cs

    if radius_scaling:
        A, B, C = np.interp(lambdas, scale_data, (0.5 * radius, 1.5 * radius))
    else:
        A, B, C = radius, radius, radius
    X = A * cs(v, 2 / r) * cs(u, 2 / r)
    Y = B * cs(v, 2 / s) * sn(u, 2 / s)
    Z = C * sn(v, 2 / t)
    return X, Y, Z


def Kindlmann_glyph(coordinates, lambdas, radius, scale_data, shape='cuboid', concavity=False, radius_scaling=False):
    u, v = coordinates
    u = u + np.pi
    v = v + np.pi / 2
    r, s, t = np.sort(np.abs(lambdas))[::-1]
    # r, s, t = lambdas
    if radius_scaling:
        A, B, C = np.interp(lambdas, scale_data, (0.5 * radius, 1.5 * radius))
    else:
        A, B, C = radius, radius, radius
    Cl = (r - s) / sum([r, s, t])
    Cp = 2 * (s - t) / sum([r, s, t])
    Cs = 3 * t / sum([r, s, t])
    gamma = 3
    if Cl >= Cp:
        alpha = (1 - Cp) ** gamma
        betta = (1 - Cl) ** gamma
        # X = A * g(u, alpha) * f(v, betta)
        # Y = B * f(u, alpha) * f(v, betta)
        # Z = C * g(v, betta)
        X = A * cs(v, betta)
        Y = - B * sn(u, alpha) * sn(v, betta)
        Z = A * cs(u, alpha) * sn(v, betta)
    else:
        alpha = (1 - Cl) ** gamma
        betta = (1 - Cp) ** gamma
        X = A * cs(u, alpha) * sn(v, betta)
        Y = B * sn(u, alpha) * sn(v, betta)
        Z = C * cs(v, betta)
    return X, Y, Z


def Kindlmann_modified_glyph(coordinates, lambdas, radius, scale_data,
                             shape='cuboid', concavity=False, radius_scaling=False):
    u, v = coordinates
    u = u + np.pi
    v = v + np.pi / 2
    r, s, t = np.sort(np.abs(lambdas))[::-1]
    r, s, t = sorted(lambdas, key=abs)[::-1]
    # r, s, t = lambdas
    # print([r, s, t])
    if radius_scaling:
        A, B, C = np.interp(lambdas, scale_data, (0.5 * radius, 1.5 * radius))
    else:
        A, B, C = radius, radius, radius
    eigens_norm = np.linalg.norm(lambdas)
    # Cl = (r-s)/sum(abs([r, s, t]))
    # Cp = 2*(s-t)/sum([r, s, t])
    # Cs = 3*t/sum([r, s, t])
    # Cl, Cp, Cs = [a - abs(a) * (sum(lambdas)-1)/sum(abs(lambdas)) for a in lambdas]
    # Cl = 1.1
    # Cp = 0.2
    # Cs = 3*t/sum(lambdas)
    Cl = (r ** 2 - s ** 2) / eigens_norm ** 2
    Cp = 2 * (s ** 2 - t ** 2) / eigens_norm ** 2
    Cs = 3 * t ** 2 / eigens_norm ** 2
    gamma = 6
    if Cl >= Cp:
        alpha = np.abs(1 - Cp) ** gamma * (1.5 - np.sign(r) * np.sign(s) / 2) + (0.5 + np.sign(r) * np.sign(s) / 2)
        betta = np.abs(1 - Cl) ** gamma * (1.5 - np.sign(s) * np.sign(t) / 2) + (0.5 + np.sign(s) * np.sign(t) / 2)
        # print([alpha, betta])
        # X = A * cs(v, betta)
        # Y = - B * sn(u, alpha) * sn(v, betta)
        # Z = C * cs(u, alpha) * sn(v, betta)
        # X = A * g(u, alpha) * f(v, betta)
        # Y = B * f(u, alpha) * f(v, betta)
        # Z = C * g(v, betta)

        X = A * cs(v, betta)
        Y = - B * sn(u, alpha) * sn(v, betta)
        Z = C * cs(u, alpha) * sn(v, betta)

    else:
        alpha = np.abs(1 - Cl) ** gamma * (1.5 - np.sign(s) * np.sign(t) / 2) + (0.5 + np.sign(s) * np.sign(t) / 2)
        betta = np.abs(1 - Cp) ** gamma * (1.5 - np.sign(r) * np.sign(s) / 2) + (0.5 + np.sign(r) * np.sign(s) / 2)
        # alpha = 3
        # betta = 3
        # print([alpha, betta])
        X = A * cs(u, alpha) * sn(v, betta)
        Y = B * sn(u, alpha) * sn(v, betta)
        Z = C * cs(v, betta)
    return X, Y, Z


"""
def plot_glyph(center, data, limits):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    radius = 0.5
    x, y, z = get_glyph_data(center, data, limits, glyph_radius=radius)
    color = get_color(data, limits)
    color = 'r'
    # surf = ax.plot_surface(x, y, z, linewidth=0, antialiased=False, color=color)
    # plt.show()
    color = (0.2, 0.2, 0.2, 1)
    color = color[:3]
    mlab.mesh(x, y, z, color=color)

    # mlab.title(str(equation))
"""
