import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('log4net running')
@cli.command()
def start(): click.echo('log4net started')
if __name__ == '__main__': cli()
