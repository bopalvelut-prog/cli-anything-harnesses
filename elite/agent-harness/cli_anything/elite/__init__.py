import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elite running')
@cli.command()
def start(): click.echo('elite started')
if __name__ == '__main__': cli()
