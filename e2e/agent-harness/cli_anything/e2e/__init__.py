import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('e2e running')
@cli.command()
def start(): click.echo('e2e started')
if __name__ == '__main__': cli()
