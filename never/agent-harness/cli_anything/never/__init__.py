import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('never running')
@cli.command()
def start(): click.echo('never started')
if __name__ == '__main__': cli()
