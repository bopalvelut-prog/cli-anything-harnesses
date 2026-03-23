import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pjsua running')
@cli.command()
def start(): click.echo('pjsua started')
if __name__ == '__main__': cli()
