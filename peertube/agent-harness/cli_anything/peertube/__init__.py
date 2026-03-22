import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('PeerTube status')
@cli.command()
def videos(): click.echo('PeerTube videos')
if __name__ == '__main__': cli()
