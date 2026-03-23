import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lzo running')
@cli.command()
def start(): click.echo('lzo started')
if __name__ == '__main__': cli()
