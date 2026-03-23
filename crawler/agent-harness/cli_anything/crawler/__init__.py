import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crawler running')
@cli.command()
def start(): click.echo('crawler started')
if __name__ == '__main__': cli()
