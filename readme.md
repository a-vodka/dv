
# Algorithms and models for data collection, analysis, and visualization (Mathematical methods of data visualization)

![Logo of datavisualization](https://github.com/a-vodka/dv/raw/master/staff/dv_logo.png)

This course covers a wide spectrum of mathematical models of data visualization topics, from foundational concepts to advanced techniques. Beginning with an overview of chart types and potential misrepresentations, it proceeds to explore Python libraries, software tools, and specialized plots. The course delves into advanced domains, discussing the visualization of fields, vectors, tensors, tree structures, and graph representations. It also covers dimension reduction methods, text data visualization using LaTeX, and the principles of effective infographic design. With practical examples and comparisons, the course aims to provide a comprehensive understanding of data visualization for effective communication.

[Syllabus for 122 Computer Science](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/122-Syllabus-Data-Visualization.docx)

[Syllabus for 113 Applied Mathematics](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/113-Syllabus-Data-Visualization.docx)

## Lectures
### Topic 1. Introduction to data visualization.
Levels of visualization. Chart types: Line, Pie, Bar, Histogram, Spaghetti, Map, Steam, Bubble, Gantt, Sunburst, Polar Clock, Radar, Tag cloud, Heat map, Trees, Mind Map. How to lie with charts? Chart Junk.
- [Presentation 1](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec1-intro.pptx)

### Topic 2. Software for chart plotting in Python.
Matplotlib, Seaborn, Plotnine(ggplot), Bokeh, pygal, Plotly, geoplotlib, Gleam, missingno, Leather, Altair, Folium. 2D and 3D plots. Log scale. Box plot, Violin plot. Examples.
- [Presentation 2](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec2-matplotlib.pptx)

### Topic 3. Visualization of fields, vector, tensors
Introduction and problem statement. Scalar filed. Gradient of scalar field. Divergence and Vorticity. Vector Glyphs. Vector Color Coding. Displacement Plots. Stream Lines, Tensor glyphs, Tensor field lines, Hyperstreamlines.
- [Presentation 3a Vector Fields](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec3a-vector.pptx) 
- [Presentation 3b Tensor fields](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec3b-tensor.pptx)

### Topic 4. Tree visualization.
Historical context, first paper of tree visualization (Tutte, Knuth). Application of tree visualization (UML, Biology, Networks, Security, Social Networks). Requirements, conventions to tree visualization. D. Knuth algorithm, Theorem of area of tree laying. Tree Drawing Algorithm: Layered Drawing, Radial Drawing, HV-Drawing, Recursive Winding. Dendrogram. Balloon trees. Hyperbolic Tree. Space-filling methods: Tree map, Beamtree, Icicle.
- [Presentation 4 intro](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec4-tree-intro.pptx)
- [Presentation 5 tree layout](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec5-tree-layout.pptx)

### Topic 5. Graph visualization
Introduction and problem statement. Algorithm of graph drawing: Straight Line Drawing. Orthogonal Drawing. Grid Drawing. Circular Drawing. Polyline Drawing. Upward drawing. Sugiyama method. Force directed graph drawing (mathematical problem statement): Kamada & Kawai, Fruchterman & Reingold, Davidson & Harel.
Software for Graph visualization: NetworkX, Gephi. Examples. Visualization of large graph.
- [Presentation 6 graph layouts](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec6-graf-viz.pptx)
- [Presentation 7 networkx](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec7-networkx.pptx)
- [Presentation 8 gephi](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec8-gephi.pptx)


### Topic 6. Method of Dimension reduction
Introduction and problem statement. Linear method. PCA and SVD. Examples: Iris, Eigen Faces, MNIST. Discussion. Nonlinear method: MDS, ISOMAP, LLE, Laplacian eigenmaps, SNE, tSNE. Examples. Method comparation. Sklearn library.
- [Presentation 9 PCA + SVD](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec9-dim-reduc-PCA+SVD.pptx)
- [Presentation 10 MDS, ISOMAP, LLE, T-SNE](https://view.officeapps.live.com/op/view.aspx?src=https://github.com/a-vodka/dv/raw/master/dv-lec10-dimesion-reduction.pptx)

### Topic 7. Visualization of text data
Introduction to latex, setting up a latex document, typesetting text, handling latex errors, typesetting equations, using latex packages. Structured documents, sections, labels and cross-references, figures and tables in latex, automatic bibliographies with bibtex, useful latex packages and online resources, latex presentations with beamer, drawing in latex with tikz, tracked changes and comments with todo notes.
- [Presentation 11 Latex (overleaf) tutorial](https://github.com/a-vodka/dv/raw/master/dv-lec11-latex-tutorial.pdf)

### Topic 8. Infographics
Definition and purpose, Historical context and evolution, Importance in modern communication. Principles of Effective Infographic Design: Simplicity and clarity, Visual hierarchy, Consistency and coherence, Audience consideration. Types of Infographics: Statistical infographics, Informational infographics, Timeline infographics, Comparison infographics, Process infographics, Geographical infographics. Choosing the Right Data for Infographics: Identifying key messages, Color, Typography, and Layout. The psychology of color in communication, Typography best practices, Layout considerations for optimal readability.
- [Presentation 12 Infographics](https://github.com/a-vodka/dv/raw/master/dv-lec12-infographics.pdf)

## Laboratory task

- Task 01. [Intro to matplotlib](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab01-matplotlib.pdf)
- Task 02. [Vector and Tensor field](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab02-vector+tesor.pdf)
- Task 03. [Animation with matplotlib](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab03-animation.pdf)
- Task 04. [Binary tree](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab04-binary%20tree.pdf)
- Task 05. [Tree visualization with networkx](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab05-networkx.pdf)
- Task 06. [Gephi](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab06-gephi.pdf)
- Task 07. [Instagram followers](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab07-instagraph.pdf)
- Task 08. [Nonlinear dimension reduction](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab08-Dim%20reduction.pdf)
- Task 09. [PCA + SVD](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab09-PCA+SVD.pdf)
- Task 10. [CV+Report with latex](http://docs.google.com/gview?url=https://github.com/a-vodka/dv/raw/master/lab/lab10-latex.pdf)
