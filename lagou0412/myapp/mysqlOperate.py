import  sqlalchemy
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String #区分大小写

mysql_user = "root"
mysql_passwd = "123456"
mysql_dbname = "mydb"
#创建连接
engine=create_engine("mysql+pymysql://{}:{}@localhost/{}".format(mysql_user, mysql_passwd, mysql_dbname),encoding='utf-8',echo=True)
#生成orm基类
base=declarative_base()
class lagou_data(base):
    __tablename__ = 'lagou_data' #表名
    id = Column(Integer, primary_key=True)
    companyId = Column(String(32))
    positionName = Column(String(512))
    workYear = Column(String(128))
    education = Column(String(128))
    city = Column(String(128))
    salary = Column(String(128))
    companyShortName = Column(String(256))
    companyFullName = Column(String(256))
    formatCreateTime = Column(String(128))

    def __repr__(self):
        return self.positionName

    
headers = []

def collect_fields(classname):
    for attr in classname.__dict__.keys():
        if type(getattr(classname, attr)) == sqlalchemy.orm.attributes.InstrumentedAttribute:
            headers.append(attr)
    print(headers)

collect_fields(lagou_data)

def createTable():
    base.metadata.create_all(engine)

# 对外接口 批量
def insertValues(jonlist):
    Session_class=sessionmaker(bind=engine)
    session=Session_class()

    for jobinfo in jonlist:
        lagou_data_obj = lagou_data()
        for field in headers:
            if field in jobinfo:
                setattr(lagou_data_obj, field, jobinfo[field])
        session.add(lagou_data_obj)

    session.commit()
    session.close()

# 对外接口 单个
def insertValue(item):
    Session_class=sessionmaker(bind=engine)
    session=Session_class()

    lagou_data_obj = lagou_data()
    for field in headers:
        if field in item:
            setattr(lagou_data_obj, field, item[field])
    session.add(lagou_data_obj)

    session.commit()
    session.close()

def getData():
    Session_class=sessionmaker(bind=engine)
    session=Session_class()
    
    results = session.query(lagou_data).all()
    return results

all_data = getData()