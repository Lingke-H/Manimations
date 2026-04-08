


# 三维至二维投影数学方法可视化

本仓库包含用于生成三维至二维投影动画的 Manim 源代码及技术文档。本项目将计算机图形学背后的线性代数原理进行了可视化，主要侧重于空间旋转如何影响二维正交投影。

## 数学框架

本仓库中的动画演示了基础三维图形渲染所需的基本矩阵运算。变换流程被分解为四个离散步骤：

1.  **向量表示：** 在三维空间坐标系中定义坐标。
2.  **矩阵变换：** 应用旋转矩阵来调整视角或物体朝向。
3.  **降维：** 消除 Z 坐标（在正交投影中），以将坐标映射到平面上。
4.  **二维渲染：** 在二维屏幕上生成最终输出。

此外，本项目还重点展示了关键的数学与计算限制：
* **非交换性：** 演示矩阵乘法的顺序会改变最终的投影结果 ($R = R_x R_y R_z$)。
* **数值漂移：** 可视化连续变换中由于浮点误差导致的基向量正交性衰减现象。
* **信息丢失：** 阐明奇异投影矩阵在数学上不可逆的本质。

## 仓库结构

本仓库包含多个 Python 脚本，每个脚本负责渲染特定的数学证明或几何变换：

* **`CombinedRotation_I.py`**：主要的三维渲染脚本。它执行透明立方体绕 Z、Y 和 X 轴的连续旋转。该脚本利用了顶点追踪技术，并同步渲染出相应的复合旋转矩阵方程。
* **`CubeRotation_x.py`、`CubeRotation_y.py`、`CubeRotation_z.py`**：模块化脚本，利用 Manim 的更新器 (updater) 函数执行连续的单轴旋转。这些是复合旋转的基础组件。
* **`Orthogonal Property.py`**：专门用于几何证明的二维动画。它将正交矩阵变换应用于一组向量，以此证明正交矩阵能够保持向量的模长及向量间的夹角不变。
* **`NowWeHaveEmotions.py`**：补充脚本，利用 `manimlib` 的 Pi Creature 类来演示基于角色的渲染和属性修改。

## 安装与运行

若要在本地编译并渲染动画，需要进行以下环境配置。

### 系统要求
* Python 3.8 或更高版本
* **Manim Community Edition (CE)：** 用于编译三维立方体旋转和正交性证明脚本。
* **ManimGL：** 专门用于编译 `NowWeHaveEmotions.py` 脚本。

### 渲染说明
若要执行并渲染主要的复合旋转场景，请在终端中运行以下命令：

```bash
manim -pql CombinedRotation_I.py CubeRotation
```
*（注：将 `-pql` 标志修改为 `-pqh` 可进行高质量渲染，其他输出配置请参阅 Manim 官方文档。）*


# Mathematical Methods for 3D-to-2D Projection Visualized

This repository contains the Manim source code and technical documentation used to generate 3D-to-2D projection animations. The project visualizes the linear algebra principles underlying computer graphics, specifically focusing on how spatial rotations affect 2D orthographic projections.

## Mathematical Framework

The animations contained in this repository illustrate the fundamental matrix operations required for basic 3D graphics rendering. The transformation pipeline is broken down into four discrete steps:

1.  **Vector Representation:** Defining coordinates in a 3D spatial coordinate system.
2.  **Matrix Transformation:** Applying rotation matrices to adjust the viewpoint or object orientation.
3.  **Dimensionality Reduction:** Eliminating the Z-coordinate (in orthographic projection) to map coordinates to a plane.
4.  **2D Rendering:** Generating the final output on a 2D screen.

Additionally, the project highlights key mathematical and computational constraints:
* **Non-Commutativity:** Demonstrating that the order of matrix multiplication alters the final projection result ($R = R_x R_y R_z$).
* **Numerical Drift:** Visualizing the degradation of orthogonality due to floating-point errors over continuous transformations.
* **Information Loss:** Illustrating the mathematically irreversible nature of singular projection matrices.

## Repository Structure

The repository consists of several Python scripts, each responsible for rendering specific mathematical proofs or geometric transformations:

* **`CombinedRotation_I.py`**: The primary 3D rendering script. It executes a sequential rotation of a transparent cube across the Z, Y, and X axes. The script utilizes vertex tracking and simultaneously renders the corresponding combined rotation matrix equations.
* **`CubeRotation_x.py`, `CubeRotation_y.py`, `CubeRotation_z.py`**: Modular scripts utilizing Manim's updater functions to execute continuous, single-axis rotations. These serve as the foundational elements for the combined rotation.
* **`Orthogonal Property.py`**: A 2D animation dedicated to a geometric proof. It applies an orthogonal matrix transformation to a set of vectors to establish that orthogonal matrices preserve both vector magnitude and the angle between vectors.
* **`NowWeHaveEmotions.py`**: A supplementary script utilizing the `manimlib` Pi Creature class to demonstrate character-based rendering and attribute manipulation.

## Installation and Execution

To compile and render the animations locally, the following environment setup is required.

### System Requirements
* Python 3.8 or higher
* **Manim Community Edition (CE):** Required for compiling the 3D cube rotations and orthogonal property proofs.
* **ManimGL:** Required specifically for compiling `NowWeHaveEmotions.py`.

### Rendering Instructions
To execute the primary combined rotation scene in high quality, run the following command in the terminal:

```bash
manim -pql CombinedRotation_I.py CubeRotation
```
