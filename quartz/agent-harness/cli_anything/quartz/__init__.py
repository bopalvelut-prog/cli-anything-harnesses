import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quartz running')
@cli.command()
def start(): click.echo('quartz started')
if __name__ == '__main__': cli()
