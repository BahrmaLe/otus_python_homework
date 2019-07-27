import psycopg2
import pytest
from sshtunnel import SSHTunnelForwarder


class SSHConnector:

    def __init__(self):
        self.tunnel = SSHTunnelForwarder(('192.168.56.103', 22),
                                         ssh_username='akuksenko',
                                         ssh_password='toor',
                                         remote_bind_address=('192.168.56.103', 5432),
                                         local_bind_address=('localhost', 6543))

    def start_tunnel(self):
        """Create an SSH tunnel"""
        self.tunnel = SSHTunnelForwarder(('192.168.56.103', 22),
                                         ssh_username='akuksenko',
                                         ssh_password='toor',
                                         remote_bind_address=('192.168.56.103', 5432),
                                         local_bind_address=('localhost', 6543))
        self.tunnel.start()

    def stop_tunnel(self):
        """Create an SSH tunnel"""
        self.tunnel.stop()


@pytest.fixture()
def db_connect():
    """Create a database connection"""
    conn = psycopg2.connect(database='opencart', user='ocuser', password='PASSWORD', host='192.168.56.103')
    cur = conn.cursor()
    conn.execute("INSERT INTO `oc_product` (`product_id`, `model`, `sku`, `upc`, `ean`, `jan`, `isbn`, `mpn`, "
                 "`location`, `quantity`, `stock_status_id`, `image`, `manufacturer_id`, `shipping`, `price`, "
                 "`points`, `tax_class_id`, `date_available`, `weight`, `weight_class_id`, `length`, `width`, "
                 "`height`, `length_class_id`, `subtract`, `minimum`, `sort_order`, `status`, `viewed`, "
                 "`date_added`, `date_modified`, `oct_product_stickers`) VALUES ('51','Бумажные обои','ES80501',"
                 "'', '', '', '', '','Москва','245','5','catalog/main/big_ES80501.jpg','','1','4278','0', '0', "
                 "'2017-01-29', '0.00000000', '1','8.23','0.68','0.53','1', '1', '1', '1', '1', '0', '2017-01-29 "
                 "17:50:53', '2017-01-29 23:02:00', '')")
    conn.commit()
    result = cur.fetchall()
    print(result)
    conn.close()
    return result
