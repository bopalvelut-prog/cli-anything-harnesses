import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oracle_db running')
@cli.command()
def start(): click.echo('oracle_db started')
if __name__ == '__main__': cli()
