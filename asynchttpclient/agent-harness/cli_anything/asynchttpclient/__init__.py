import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asynchttpclient running')
@cli.command()
def start(): click.echo('asynchttpclient started')
if __name__ == '__main__': cli()
