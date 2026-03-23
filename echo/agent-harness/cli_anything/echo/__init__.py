import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('echo running')
@cli.command()
def start(): click.echo('echo started')
if __name__ == '__main__': cli()
