import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aerogear running')
@cli.command()
def start(): click.echo('aerogear started')
if __name__ == '__main__': cli()
