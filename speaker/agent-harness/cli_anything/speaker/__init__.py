import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('speaker running')
@cli.command()
def start(): click.echo('speaker started')
if __name__ == '__main__': cli()
