import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("A simple task list")
st.write("This ap will hopefully help you with your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "Enter a To-Do:",
              on_change=add_todo, key='new_todo')


