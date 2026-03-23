import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('root running')
@cli.command()
def start(): click.echo('root started')
if __name__ == '__main__': cli()
