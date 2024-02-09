class Product: 
      
    def get_id(self): 
        return self.id 
        
    def get_marca(self): 
        return self.marca 
      
    def set_marca(self, marca): 
        self.marca = marca
        
    def get_nome(self): 
        return self.nome 
      
    def set_nome(self, nome): 
        self.nome = nome
        
    def get_prezzo(self): 
        return self.prezzo 
      
    def set_prezzo(self, prezzo): 
        self.prezzo = prezzo
        
    def find_products():
        mydb = dbmanager.connection(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM customers")

        myresult = mycursor.fetchall()
        
