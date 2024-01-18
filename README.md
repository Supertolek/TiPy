# TiPy generator

https://supertolek.github.io/TiPy/README.md

> ### What is Ti advanced?
> TiPy is a way to make the cration of Ti-basic programms easyer.
> 
> ⚠️This documentation was made for an older version on TiPy

## Structure

<style>key{font-weight:bold;color:#CE6A6B;}class{color:#EBACA2}var{color:#4A919E}code{background-color:#f2f2f2;border-radius:5px;padding-left:3px;padding-right:3px;}critical{font-weight:bold;color:red}</style>

- A line of Ti extended is composed of a [key](#keywords), and the arguments needed: <code><key>key</key> _arguments_</code>
- There is librairies which add keywords. To use them, you have to write: <code><class>list</class>.<key>add</key> <var>_name_</var> _value_</code>
- To add a comment, write // Comment, # Comment or /* Comment */
- To create a constant, write <code><key>cst</key> <class>_type_</class> <var>_value_</var></code>. You can create constants for <code><class>numbers</class></code>, <code><class>text</class></code>, <code><class>list</class></code>, <code><class>matrix</class></code>, <code><class>vector</class></code>, <code><class>boolean</class></code>, <code><class>color</class></code> and <code><class>math</class></code>.
- To create a function constant, write:<br><code><key>cst</key> <critical>!</critical> <class>func</class> <var>_function_</var></code><br><code>---</code><br><code><key>code</key> <class>args</class></code><br><code>---</code><br>_(No <code><key>\_ </key></code> nedded)_

## Index

- [Variables part](#variables)
- [Controls part](#controls)
- [Interactions part](#interactions)
- [Draw part](#draw)
- [Librairies part](#librairies)
- [Other](#other-ti-basic-functions)

## Variables

### Variables types

| Type   | Content                   | Part                    |
| ------ | ------------------------- | ----------------------- |
| int    | Number (integer or float) | [number](#number)       |
| str    | Text                      | [text](#text)           |
| list   | List                      | [list](#list)           |
| matrix | Matrix                    | [matrix](#matrix)       |
| pict   | Image                     | [picture](#picture)     |
| vect   | Vector 2d/3d              | [vector](#vector)       |
| bool   | Boolean                   | [boolean](#boolean)     |
| color  | Color                     | [color](#colors)        |
| func   | Functions                 | [functions](#functions) |
| math   | Math functions            | [math](#math-functions) |

For every type (except boolean), you can delete a variable using <code><critical>del</critical> <class>_type_</class> <var>_name_</var></code>.

### Number

There is 27 numbers variables available: letters from A to Z and θ (thêta).

| Action           | Syntax |
| ---------------- | ------ |
| Declaration      | <code><key>new</key> <class>int</class> <var>_number_</var> <class>int</class> <var>_value_</var></code>                  |
| Changing value   | <code><key>set</key> <class>int</class> <var>_number_</var> <class>int</class> <var>_value_</var></code>                  |
| Increasing       | <code><key>inc</key> <class>int</class> <var>_number_</var> <class>int</class> <var>_value_</var> _(1 by default)_</code> |
| Other operations | <code><key>calc</key> <class>int</class> <var>_number_</var> _operation (for exemple: 3*{<var>_name_</var>})_</code>      |

### Text

There is 10 text variables available: from chn0 to chn9.

| Action         | Syntax |
| -------------- | ------ |
| Declaration    | <code><key>new</key> <class>str</class> <var>_string_</var> <class>str</class> <var>_text_</var></code> |
| Changing value | <code><key>set</key> <class>str</class> <var>_string_</var> <class>str</class> <var>_text_</var></code> |

### List

There is 6 existing list variables: from L<sub>1</sub> to L<sub>6</sub>.

There is a pretty infinite amount of undeclared lists: L1, L2...

| Action         | Syntax |
| -------------- | ------ |
| Declaration    | <code><key>new</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var></code>                                                                       |
| Changing value | <code><key>set</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var></code>                                                                       |
| Changing item  | <code><class>list</class>.<key>replace</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var> <class>vector2d</class> <var>_position_</var></code> |
| Append list    | <code><class>list</class>.<key>append</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var></code>                                                |
| Inserting item | <code><class>list</class>.<key>insert</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var> <class>vector2d</class> <var>_position_</var></code>  |
| Fill list      | <code><class>list</class>.<key>fill</key> <class>list</class> <var>_list_</var> <class>int</class> <var>_value_</var></code>                                                  |
| Concat         | <code><class>list</class>.<key>concat</key> <class>list</class> <var>_list_</var> <class>list</class> <var>_list_</var></code>                                                |

### Matrix

There is 10 matrix variables available: from [A] to [J]

| Action                  | Syntax |
| ------------------      | ------ |
| Declaration             | <code><key>new</key> <class>matrix</class> <var>_matrix_</var> <class>matrix</class> <var>_matrix_</var></code>                                                                                          |
| To list                 | <code><key>set</key> <critical>!</critical> <class>list</class> <var>_list_</var> <class>matrix</class> <var>_matrix_</var></code>                                                                       |
| Dimentions              | <code><class>matrix</class>.<key>dim</key> <class>matrix</class> <var>_matrix_</var> (_-> <class>vector2d</class>_)</code>                                                                               |
| Exchange rows           | <code><class>matrix</class>.<key>swap</key> <class>matrix</class> <var>_matrix_</var> <class>int</class> <var>_row1_</var> <class>int</class> <var>_row2_</var></code>                                   |
| Add two rows            | <code><class>matrix</class>.<key>add</key> <class>matrix</class> <var>_matrix_</var> <class>int</class> <var>_row1_</var> <class>int</class> <var>_row2_</var> _(-> <class>matrix</class>)_</code>       |
| Multiply row with value | <code><class>matrix</class>.<key>multiply</key> <class>matrix</class> <var>_matrix_</var> <class>int</class> <var>_row1_</var> <class>int</class> <var>_value_</var> _(-> <class>matrix</class>)_</code> |

### Picture

There is 10 picture variables available: from Pic0 to pic9

_(act on the graph background)_

| Action          | Syntax |
| --------------- | ------ |
| Save picture    | <code><class>picture</class>.<key>save</key> <class>int</class> <var>_imgindex_</var></code> |
| Show picture    | <code><class>picture</class>.<key>show</key> <class>int</class> <var>_imgindex_</var></code> |
| Show background | <code><key>sbg</key> <class>int</class> <var>_bgindex_</var></code>                          |
| Hide background | <code><key>hbg</key></code> |

### Vector

Vector variables are stored in a list.

| Action         | Syntax |
| -------------- | ------ |
| Declaration    | <code><key>new</key> [<class>vector2d</class>\|<class>vector3d</class>] <var>_vector_</var> [<class>vector2d</class>\|<class>vector3d</class>] <var>_vector_</var></code> |
| Changing value | <code><key>set</key> [<class>vector2d</class>\|<class>vector3d</class>] <var>_vector_</var> [<class>vector2d</class>\|<class>vector3d</class>] <var>_vector_</var></code> |
| Get value      | <code>[<class>vector2d</class>\|<class>vector3d</class>].get [<class>vector2d</class>\|<class>vector3d</class>] <var>_name_</var> [_x_\|_y_\|_z_\|]                       |

> A vector is writen like this: <code><class>[<class>vector2d</class>\|<class>vector3d</class>]</class> <var>_x_ _y_ _z_</var></code>
> 
> Or like this: <code><var><_x_, _y_, _z_></var></code>

### Boolean

Boolean variables are stored in a list.

| Action         | Syntax |
| -------------- | ------ |
| Declaration    | <code><key>new</key> <class>bool</class> <var>_boolean_</var> <class>bool</class> <var>_boolean_</var></code> |
| Changing value | <code><key>set</key> <class>bool</class> <var>_boolean_</var> <class>bool</class> <var>_boolean_</var></code> |
| Invert         | <code><class>bool</class>.<key>invert</key> <class>bool</class> <var>_boolean_</var></code>                   |

### Colors

To get a color, use <code><class>colors</class>.<var>_color_</var></code>

### Functions

You can create as many functions as you want, they are coded into the file.

| Action      | Syntax |
| ----------- | ------ |
| Declaration | <code><key>def</key> <class>func</class> <var>_function_</var> <class>list</class> <var>_args_</var></code> |
| Return      | <code><key>back</key> <class>_type_</class> <var>_value_</var></code>                                       |
| Less related         |
| Go to       | <code><key>goto</key> <class>int</class> <var>_line_</var></code>                                           |
| Execute     | <code><key>exe</key> <class>str</class> <var>_programm_</var></code>                                        |


### Math functions

You can create 9 math functions: from Y<sub>0</sub> to Y<sub>9</sub>.

| Action         | Syntax |
| -------------- | ------ |
| Declaration    | <code><key>new</key> <class>math</class> <var>_mathfunction_</var> <class>math</class> <var>_value_</var></code> |
| Changing value | <code><key>set</key> <class>math</class> <var>_mathfunction_</var> <class>math</class> <var>_value_</var></code> |

## Controls

Indentation is replaced by <code><key>_</key> _code_</code>

| Statement        | Syntax |
| ---------------- | ------ |
| If               | <code><key>if</key> <class>_type_</class> <var>_value_</var> <class>calc</class> <var>_operation_</var> <class>_type_</class> <var>_value_</var></code>                                   |
| Elif             | <code><key>elif</key> <class>_type_</class> <var>_value_</var> <class>calc</class> <var>_operation_</var> <class>_type_</class> <var>_value_</var></code>                                 |
| Else             | _No argument_                                                                                                                                                                             |
| For              | <code><key>for</key> <class>int</class> <var>_number_</var> in <class>int</class> <var>_start_</var> <class>int</class> <var>_end_</var> <class>int</class> <var>_increment_</var></code> |
| Foreach          | <code><class>list</class>.<key>foreach</key> <class>int</class> <var>_number_</var> in <class>_iterable_</class> <var>list</var></code>                                                   |
| While            | <code><key>while</key> <class>_type_</class> <var>_value_</var> <class>calc</class> <var>_operation_</var> <class>_type_</class> <var>_value_</var></code>                                |
| While not        | <code><key>!while</key> <class>_type_</class> <var>_value_</var> <class>calc</class> <var>_operation_</var> <class>_type_</class> <var>_value_</var></code>                               |
| Pause            | <code><key>pause</key> <class>_type_</class> <var>_value_</var></code>                                                                                                                    |
| Stop all         | <code><critical>stop</critical></code>                                                                                                                                                    |
| Stop subprogramm | <code><critical>ret</critical></code>                                                                                                                                                     |
| Type             | <code><key>type</key> <var>_variable_</var>                                                                                                                                               |

## Interactions

| Action     | Syntax |
| ---------- | ------ |
| Output     | <code><key>out</key> <class>_type_</class> <var>_value_</var> <class>int</class> <var>_x_</var> <class>int</class> <var>_y_</var></code>                                                              |
| Ask choice | <code><key>ask</key> <class>_type_</class> <var>_question_</var> <class>_type_</class> <var>_choice1_</var> <class>func</class> <var>_action_</var></code> _You can add as many options as you want._ |
| Input      | <code><key>inp</key> <class>_type_</class> <var>_variable_</var> <class>_type_</class> <var>_question_</var> <class>bool</class> <var>_prompt_</var></code>                                                                          |
| Get key    | <code><class>keyboard</class>.<key>get</key> (-> <class>int</class>)</code>                                                                                                                           |
| Clear      | <code><key>clr</key></code>                                                                                                                                                                           |
| Send var   | <code><class>usb</class>.<key>send</key> <class>_type_</class> <var>_variable_</var></code>                                                                                                           |

## Draw

| Action          | Syntax |
| --------------- | ------ |
| Erase           | <code><class>draw</class>.<key>clear</key>                                                                                                                                        |
| Line            | <code><class>draw</class>.<key>line</key> <class>vector2d</class> <var>_point1_</var> <class>vector2d</class> <var>_point2_</var> <class>colors</class>.<var>_color_</var></code> |
| Horizontal line | <code><class>draw</class>.<key>horizontal</key> <class>int</class> <var>_position_</var> <class>colors</class>.<var>_color_</var></code>                                          |
| Vertical line   | <code><class>draw</class>.<key>vertical</key> <class>int</class> <var>_position_</var> <class>colors</class>.<var>_color_</var></code>                                            |
| Draw function   | <code><class>draw</class>.<key>drawfunc</key> <class>math</class> <var>_function_</var></code>                                                                                                                   |
| Circle          | <code><class>draw</class>.<key>circle</key> <class>vector2d</class> <var>_center_</var> <class>int</class> <var>_radius_</var> <class>colors</class>.<var>_color_</var></code>    |
| Text            | <code><class>draw</class>.<key>text</key> <class>int</class> <var>_line_</var> <class>int</class> <var>_column_</var> <class>str</class> <var>_text_</var></code>                 |
| Set pixel       | <code><class>draw</class>.<key>pixel</key> <class>vector2d</class> <var>_position_</var> <class>system</class> [set\|none\|edit] <class>colors</class>.<var>_color_</var></code>  |
| Set point       | <code><class>draw</class>.<key>point</key> <class>vector2d</class> <var>_position_</var> <class>system</class> [set\|none\|edit] <class>colors</class>.<var>_color_</var></code>  |


## Librairies

| Action     | Syntax |
| ---------- | ------ |
| Import     | <code><key>using</key> <class>str</class> <var>_librairy_</var></code> |
| Use var    | <code><class>_librairy_</class>.<var>location</var>
| Execute    | <code><class>_librairy_</class></code>                                     |

Included librairies :
- list
- bool
- keyboard
- usb
- colors
- draw
- viewport

## Other Ti basic functions

To run another Ti basic function, use <code><key>run</key> <class>func</class> <var>_function_</var></code>.

Like this, the function will be directly writen into the programm.
