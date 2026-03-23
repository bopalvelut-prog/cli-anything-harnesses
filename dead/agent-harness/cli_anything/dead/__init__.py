import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dead running')
@cli.command()
def start(): click.echo('dead started')
if __name__ == '__main__': cli()
