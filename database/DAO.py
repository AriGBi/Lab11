from database.DB_connect import DBConnect
from model.Edge import Edge
from model.prodotti import Prodotto


class DAO():

    @staticmethod
    def getAllColor():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct(gp.Product_color) as c
from go_products gp 

                 
        """

        cursor.execute(query)
        for row in cursor:
            result.append(row["c"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProdotticonCOLORE(colore):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from go_products gp
                    where gp.Product_color = %s


            """

        cursor.execute(query, (colore,))
        for row in cursor:
            result.append(Prodotto(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllEdges(colore,anno,idMap):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """  select t.Product_number as p1 , v.Product_number as p2, count(*) as peso
from(select gds.Product_number , gds.`Date` , gds.Retailer_code  from go_daily_sales gds , go_products gp  where gds.Product_number =gp.Product_number and gp.Product_color =%s) t, (select gds.Product_number , gds.`Date` , gds.Retailer_code from go_daily_sales gds , go_products gp 
where gds.Product_number =gp.Product_number and gp.Product_color =%s)v
where t.`Date` = v.`Date` and year(v.`Date`) = %s
and t.Product_number>v.Product_number and t.Retailer_code = v.Retailer_code
group by t.Product_number,  v.Product_number

                   """

        cursor.execute(query, (colore,colore,anno))
        for row in cursor:
            result.append(Edge(idMap[row["p1"]],idMap[row["p2"]],row["peso"]))
        cursor.close()
        conn.close()
        return result

