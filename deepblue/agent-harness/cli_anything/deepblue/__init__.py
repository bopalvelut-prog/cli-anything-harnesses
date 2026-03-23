import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deepblue running')
@cli.command()
def start(): click.echo('deepblue started')
if __name__ == '__main__': cli()
