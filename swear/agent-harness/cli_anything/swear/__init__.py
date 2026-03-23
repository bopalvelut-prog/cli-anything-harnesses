import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('swear running')
@cli.command()
def start(): click.echo('swear started')
if __name__ == '__main__': cli()
