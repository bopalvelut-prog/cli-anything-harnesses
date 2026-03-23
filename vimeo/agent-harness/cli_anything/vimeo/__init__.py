import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vimeo running')
@cli.command()
def start(): click.echo('vimeo started')
if __name__ == '__main__': cli()
