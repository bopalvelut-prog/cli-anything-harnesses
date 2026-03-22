
import click, mysql.connector, json, os
@click.group()
def cli(): pass
def conn(): return mysql.connector.connect(host='localhost', user='root', password=os.getenv('MYSQL_PWD',''))
@cli.command()
@click.argument('query')
def query(query):
    c = conn().cursor(); c.execute(query); click.echo(json.dumps(c.fetchall(), default=str))
@cli.command()
def databases():
    c = conn().cursor(); c.execute('SHOW DATABASES')
    for r in c.fetchall(): click.echo(r[0])
if __name__ == '__main__': cli()
