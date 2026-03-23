import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('front running')
@cli.command()
def start(): click.echo('front started')
if __name__ == '__main__': cli()
