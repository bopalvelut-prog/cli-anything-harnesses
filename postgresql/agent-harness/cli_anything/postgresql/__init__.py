
import click, psycopg2, json, os
@click.group()
def cli(): pass
def conn(): return psycopg2.connect(os.getenv('DATABASE_URL', 'postgresql://localhost/test'))
@cli.command()
@click.argument('query')
def query(query):
    c = conn().cursor(); c.execute(query); click.echo(json.dumps(c.fetchall(), default=str))
@cli.command()
def tables():
    c = conn().cursor(); c.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
    for r in c.fetchall(): click.echo(r[0])
if __name__ == '__main__': cli()
