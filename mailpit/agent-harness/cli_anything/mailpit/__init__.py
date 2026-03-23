import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mailpit running')
@cli.command()
def start(): click.echo('mailpit started')
if __name__ == '__main__': cli()
