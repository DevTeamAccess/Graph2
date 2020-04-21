
import logging
from dotenv import load_dotenv, find_dotenv
from . import option 
logger=logging.getLogger(__name__)
load_dotenv(find_dotenv(usecwd=True),verbose=True)
from  Project1.Run import run
import click
@click.group()
@option.env
def cli(env):
    pass
@cli.command()
@option.Db
@option.Db_host
@option.Db_pass
@option.Db_port
@option.Db_user
def Runapp(database,host,password,port,user):
    
    logger.warning(f'Fetcha database "{database}"')
    logger.warning(f'Fetcha host "{host}"')
    run()
    

