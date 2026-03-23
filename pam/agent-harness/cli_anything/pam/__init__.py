import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pam running')
@cli.command()
def start(): click.echo('pam started')
if __name__ == '__main__': cli()
