import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jade running')
@cli.command()
def start(): click.echo('jade started')
if __name__ == '__main__': cli()
