import tkinter
import tkinter.ttk
from database_config import *
from tkinter import messagebox


class LibraryManagement:

    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System")
        self.window.geometry("600x600")
        self.home_page()

        self.book_id = tkinter.StringVar()
        self.book_name = tkinter.StringVar()
        self.author_name = tkinter.StringVar()
        self.genre_name = tkinter.StringVar()
        self.publication_name = tkinter.StringVar()

        self.search_value = tkinter.StringVar()


    def home_page(self):

        # ==================Home Page Frame====================

        label_title = tkinter.Label(self.window,
                                    text="LIBRARY MANAGEMENT SYSTEM",
                                    bg="grey",
                                    fg="light green",
                                    bd=2,
                                    relief="solid",
                                    font=("Times New Roman", 20, "bold"),
                                    padx=2,
                                    pady=6
                                    )
        label_title.pack(side="top", fill="x")

        frame1 = tkinter.Frame(self.window,
                               bd=1,
                               relief="solid",
                               bg="grey",
                               pady=50
                               )
        frame1.place(x=0, y=50, width=600, height=550)

        add_button = tkinter.Button(frame1,
                                    padx=2, pady=2,
                                    bd=1,
                                    relief="solid",
                                    text="ADD BOOKS",
                                    font=("Times New Roman", 15, "bold"),
                                    fg="green",
                                    command=lambda: self.load_add_frame()
                                    )
        add_button.pack(pady=20)

        search_book_button = tkinter.Button(frame1,
                                       padx=2, pady=2,
                                       bd=1,
                                       relief="solid",
                                       text="SEARCH BOOKS",
                                       font=("Times New Roman", 15, "bold"),
                                       fg="green",
                                       command=lambda: self.load_search_frame()
                                       )
        search_book_button.pack(pady=20)

        issue_button = tkinter.Button(frame1,
                                      padx=2, pady=2,
                                      bd=1,
                                      relief="solid",
                                      text="ISSUE BOOKS",
                                      font=("Times New Roman", 15, "bold"),
                                      fg="green",
                                      command=lambda: self.load_issue_frame()
                                      )
        issue_button.pack(pady=20)

        view_button = tkinter.Button(frame1,
                                     padx=2, pady=2,
                                     bd=1,
                                     relief="solid",
                                     text="VIEW BOOKS",
                                     font=("Times New Roman", 15, "bold"),
                                     fg="green",
                                     command=lambda: self.load_view_frame()
                                     )
        view_button.pack(pady=20)

        logout_button = tkinter.Button(frame1,
                                       padx=2, pady=2,
                                       bd=1,
                                       relief="solid",
                                       text="LOGOUT",
                                       font=("Times New Roman", 15, "bold"),
                                       fg="green",
                                       command=lambda: self.load_logout_frame()
                                       )
        logout_button.pack(pady=20)


    # ======================ADD BOOKS FRAME=====================

    def load_add_frame(self):

        home_button = tkinter.Button(self.window,
                                     padx=2, pady=2,
                                     fg="black",
                                     text="Back to Home",
                                     font=("Times New Roman", 15, "bold"),
                                     bd=2,
                                     relief="solid",
                                     command=lambda: self.home_page()
                                     )
        home_button.pack(side="top", pady=10)

        add_frame = tkinter.LabelFrame(self.window,
                                       text="Add New Books",
                                       font=("Times New Roman", 20, "bold"),
                                       bd=5,
                                       relief="ridge",
                                       bg="grey",
                                       )
        add_frame.place(x=5, y=100, width=592, height=495)

        book_id_label = tkinter.Label(add_frame,
                                        text="Book ID: ",
                                        bg="grey",
                                        font=("Times New Roman", 15, "bold"),
                                        pady=20
                                        )
        book_id_label.grid(row=3, column=0, sticky="W")

        book_id_entry = tkinter.Entry(add_frame,
                                   font=("Times New Roman", 12, "bold"),
                                   width=50,
                                   textvariable=self.book_id
                                   )
        book_id_entry.grid(row=3, column=2)

        book_name_label = tkinter.Label(add_frame,
                                        text="Name: ",
                                        bg="grey",
                                        font=("Times New Roman", 15, "bold"),
                                        pady=20
                                        )
        book_name_label.grid(row=4, column=0, sticky="W")

        book_name_entry = tkinter.Entry(add_frame,
                                   font=("Times New Roman", 12, "bold"),
                                   width=50,
                                   textvariable=self.book_name
                                   )
        book_name_entry.grid(row=4, column=2)

        author_label = tkinter.Label(add_frame,
                                     text="Authors: ",
                                     bg="grey",
                                     font=("Times New Roman", 15, "bold"),
                                     pady=20
                                     )
        author_label.grid(row=6, column=0, sticky="W")

        author_entry = tkinter.Entry(add_frame,
                                     font=("Times New Roman", 12, "bold"),
                                     width=50,
                                     textvariable=self.author_name
                                     )
        author_entry.grid(row=6, column=2)

        genre_label = tkinter.Label(add_frame,
                                    text="Genre: ",
                                    bg="grey",
                                    font=("Times New Roman", 15, "bold"),
                                    pady=20
                                    )
        genre_label.grid(row=8, column=0, sticky="W")

        genre_entry = tkinter.Entry(add_frame,
                                    font=("Times New Roman", 12, "bold"),
                                    width=50,
                                    textvariable=self.genre_name
                                    )
        genre_entry.grid(row=8, column=2)

        publication_label = tkinter.Label(add_frame,
                                          text="Publication: ",
                                          bg="grey",
                                          font=("Times New Roman", 15, "bold"),
                                          pady=20
                                          )
        publication_label.grid(row=10, column=0, sticky="W")

        publication_entry = tkinter.Entry(add_frame,
                                          font=("Times New Roman", 12, "bold"),
                                          width=50,
                                          textvariable=self.publication_name
                                          )
        publication_entry.grid(row=10, column=2)

        add_button = tkinter.Button(add_frame,
                                    padx=2, pady=2,
                                    bd=1,
                                    relief="solid",
                                    text="ADD",
                                    font=("Times New Roman", 15, "bold"),
                                    fg="black",
                                    command=lambda: self.add_book(self.book_name, self.author_name, self.genre_name, self.publication_name, self.book_id)
                                    )
        add_button.place(x=250, y=380, width=80)

    def add_book(self, book_name, author_name, genre_name, publication_name, book_id):

        query = f"Insert into books VALUE('{book_name.get()}', '{author_name.get()}', '{genre_name.get()}', '{publication_name.get()}', {self.book_id.get()});"
        query_status = database_cursor(query)

        if query_status == True:
            messagebox.showinfo("Success", "Book Inserted Successfully!")
        else:
            messagebox.showinfo("Failure", "Error while Inserting!")


    # ======================SEARCH BOOKS FRAME=====================

    def load_search_frame(self):

        home_button = tkinter.Button(self.window,
                                     padx=2, pady=2,
                                     fg="black",
                                     text="Back to Home",
                                     font=("Times New Roman", 15, "bold"),
                                     bd=2,
                                     relief="solid",
                                     command=lambda: self.home_page()
                                     )
        home_button.pack(side="top", pady=10)

        self.search_frame = tkinter.LabelFrame(self.window,
                                       text="Search New Books",
                                       font=("Times New Roman", 20, "bold"),
                                       bd=5,
                                       relief="ridge",
                                       bg="grey",
                                       pady=20
                                       )
        self.search_frame.place(x=5, y=100, width=592, height=495)

        search_entry = tkinter.Entry(self.search_frame,
                                          font=("Times New Roman", 15, "bold"),
                                          width=40,
                                          textvariable=self.search_value,
                                          )
        search_entry.grid(row=3, column=0, padx=20)

        search_button = tkinter.Button(self.search_frame, 
                                        text="Search", 
                                        font=("Times New Roman", 15, "bold"),
                                        bd=2,
                                        relief='solid',
                                        command=lambda: self.search_result(self.search_value)
                                        )
        search_button.grid(row=3, column=1)

    def search_result(self, search_value):

        query = f"""SELECT * FROM books 
                    WHERE name='{search_value.get()}' OR author='{search_value.get()}' OR genre='{search_value.get()}' OR publication='{search_value.get()}' OR id='{search_value.get()}';"""

        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lms_db"
        )
        db_cursor = connection.cursor()
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        if len(rows) != 0:
            search_table_frame = tkinter.Frame(self.search_frame,
                                            bd=2,
                                            relief="solid"
                                            )
            search_table_frame.place(x=5, y=50, width=572, height=382)

            x_scroll = tkinter.ttk.Scrollbar(search_table_frame, orient="horizontal")
            x_scroll.pack(side="bottom", fill="x")
            y_scroll = tkinter.ttk.Scrollbar(search_table_frame, orient="vertical")
            y_scroll.pack(side="right", fill="y")
        
            self.search_table = tkinter.ttk.Treeview(search_table_frame,
                                              columns=("name", "author", "genre", "publication", "book_id"),
                                              xscrollcommand=x_scroll.set,
                                              yscrollcommand=y_scroll.set
                                              )
        
            x_scroll.config(command=self.search_table.xview())
            y_scroll.config(command=self.search_table.yview())
        
            self.search_table.heading("name", text="Name")
            self.search_table.heading("author", text="Authors")
            self.search_table.heading("genre", text="Genre")
            self.search_table.heading("publication", text="Publication")
            self.search_table.heading("book_id", text="Book ID")
            self.search_table["show"] = "headings"
            self.search_table.pack(fill="both", expand=1)

            for record in rows:
                self.search_table.insert("", "end", values=record)

            connection.commit()
        else:
            messagebox.showinfo(f"No Result", f"No Book Found.")

        connection.close()


    # ======================ISSUE BOOKS FRAME=====================
    
    # def load_issue_frame(self):
    #     issue_frame = tkinter.Frame(self.window,
    #                                 bd=1,
    #                                 relief="solid",
    #                                 pady=50,
    #                                 bg="grey"
    #                                 )
    #     issue_frame.place(x=0, y=50, width=600, height=550)
    

    # ======================VIEW BOOKS FRAME=======================

    def load_view_frame(self):

        home_button = tkinter.Button(self.window,
                                     padx=2, pady=2,
                                     fg="black",
                                     text="Back to Home",
                                     font=("Times New Roman", 15, "bold"),
                                     bd=2,
                                     relief="solid",
                                     command=lambda: self.home_page()
                                     )
        home_button.pack(side="top", pady=10)

        view_frame = tkinter.LabelFrame(self.window,
                                        text="List of Books",
                                        font=("Times New Roman", 20, "bold"),
                                        bd=5,
                                        relief="ridge",
                                        bg="grey"
                                        )
        view_frame.place(x=5, y=100, width=592, height=495)
    
        x_scroll = tkinter.ttk.Scrollbar(view_frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        y_scroll = tkinter.ttk.Scrollbar(view_frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
    
        self.book_table = tkinter.ttk.Treeview(view_frame,
                                          columns=("name", "author", "genre", "publication", "book_id"),
                                          xscrollcommand=x_scroll.set,
                                          yscrollcommand=y_scroll.set
                                          )
    
        x_scroll.config(command=self.book_table.xview())
        y_scroll.config(command=self.book_table.yview())
    
        self.book_table.heading("name", text="Name")
        self.book_table.heading("author", text="Authors")
        self.book_table.heading("genre", text="Genre")
        self.book_table.heading("publication", text="Publication")
        self.book_table.heading("book_id", text="Book ID")
        self.book_table["show"] = "headings"
        self.book_table.pack(fill="both", expand=1)

        self.fetch_data()

    def fetch_data(self):

        query = f"SELECT * FROM books"

        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lms_db"
        )
        db_cursor = connection.cursor()
        db_cursor.execute(query)
        rows = db_cursor.fetchall()
        for record in rows:
            self.book_table.insert("", "end", values=record)

        connection.commit()
        connection.close()

    # ========================LOGOUT FRAME==========================

    # def load_logout_frame(self):
    #     logout_frame = tkinter.Frame(self.window,
    #                                  bd=1,
    #                                  relief="solid",
    #                                  pady=50,
    #                                  bg="grey"
    #                                  )
    #     logout_frame.place(x=0, y=50, width=600, height=550)


# =========================MAIN FUNCTION=========================

if __name__ == '__main__':
    window = tkinter.Tk()
    obj1 = LibraryManagement(window)
    window.mainloop()
