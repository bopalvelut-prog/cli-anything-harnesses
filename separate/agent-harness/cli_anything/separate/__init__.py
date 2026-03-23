import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('separate running')
@cli.command()
def start(): click.echo('separate started')
if __name__ == '__main__': cli()
