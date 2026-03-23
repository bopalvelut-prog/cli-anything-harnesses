import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('false running')
@cli.command()
def start(): click.echo('false started')
if __name__ == '__main__': cli()
