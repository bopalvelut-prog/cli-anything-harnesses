import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('psycopg running')
@cli.command()
def start(): click.echo('psycopg started')
if __name__ == '__main__': cli()
