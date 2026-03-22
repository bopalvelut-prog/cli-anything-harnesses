import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('db')
def open(db): subprocess.run(['sqlite3', db])
@cli.command()
@click.argument('db')
@click.argument('query')
def query(db, query): subprocess.run(['sqlite3', db, query])
@cli.command()
@click.argument('db')
def tables(db): subprocess.run(['sqlite3', db, '.tables'])
if __name__ == '__main__': cli()
