# IRONRANKING-PROJECT 
----------

## **¡Bienvenidos a mi api Ironranking!**


![](https://cdn.pixabay.com/photo/2017/03/26/10/45/welcome-2175196_1280.jpg)


En este proyecto se crea una api para conocer los diferentes estudiantes del bootcamp de Data en Ironhack Madrid-0820 y algunos datos sobre los labs (y sus pull request correspondiente) que se realizan durante este.

**📌¡¡¡¡¡Spoiler Alert!!!!** : En los endpoints de *"/lab.."* encontrarás muchos MUCHOS memes frikis. 

De nada 😌
______________


## **Pero...¿cómo se utiliza?**

La url de base de la API sería *http://0.0.0.0:3000* ya que el Puerto 3000 es el que hemos utilizado en el local.

### **Endpoints:**
La API cuenta con 5 endpoints:
- **/student/create/**(*ESTUDIANTE*):

Este endopoint crea en la base de datos directamente un nuevo estudiante. ¡El que tu elijas!
- **/student/all**: 

Muestra una lista de todos los estudiantes que pertenecen a esta edición del bootcamp
- **/lab/create/**(*ESTUDIANTE*): 

Al igual que el primero, crea un lab nuevo en la base de datos con el nombre que tu elijas.
- **/lab/**( *NOMBRE DEL LAB*)**/meme**:(Empieza lo interesante)

Mostrará la URL de un meme aleatorio elegido entre todas las pull request del lab elegido.

- **"/lab/**( *NOMBRE DEL LAB*)**/search**:

Muestra una serie de datos como el número de pull request abiertas o cerradas, una lista de memes utilizados en el lab, y el tiempo del profesor para corregir cada lab.

------
-------


<img align="center" width="300" height="200" src=https://user-images.githubusercontent.com/57899051/92743489-def23480-f380-11ea-950f-939509b20ae0.jpg>











