import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sq running')
@cli.command()
def start(): click.echo('sq started')
if __name__ == '__main__': cli()
