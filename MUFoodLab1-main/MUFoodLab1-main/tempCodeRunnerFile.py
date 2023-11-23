def delete_data(self):
        con = pymysql.connect(host="localhost",user = "root",password = "",database="customer")
        cur = con.cursor()
        cur.execute("delete * from customer where Card No = %s",self.card_number.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()