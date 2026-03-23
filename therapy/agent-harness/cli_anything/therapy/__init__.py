import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('therapy running')
@cli.command()
def start(): click.echo('therapy started')
if __name__ == '__main__': cli()
