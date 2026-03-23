import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reach running')
@cli.command()
def start(): click.echo('reach started')
if __name__ == '__main__': cli()
