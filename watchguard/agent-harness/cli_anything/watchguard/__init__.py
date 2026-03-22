import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('WatchGuard running')
@cli.command()
def policies(): click.echo('Firewall policies')
if __name__ == '__main__': cli()
