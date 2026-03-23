import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ngrok running')
@cli.command()
def start(): click.echo('ngrok started')
if __name__ == '__main__': cli()
