import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('positive running')
@cli.command()
def start(): click.echo('positive started')
if __name__ == '__main__': cli()
