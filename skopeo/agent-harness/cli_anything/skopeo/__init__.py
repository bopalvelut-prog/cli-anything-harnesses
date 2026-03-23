import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('skopeo running')
@cli.command()
def start(): click.echo('skopeo started')
if __name__ == '__main__': cli()
