import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toe running')
@cli.command()
def start(): click.echo('toe started')
if __name__ == '__main__': cli()
