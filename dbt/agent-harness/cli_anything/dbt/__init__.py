import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dbt running')
@cli.command()
def start(): click.echo('dbt started')
if __name__ == '__main__': cli()
