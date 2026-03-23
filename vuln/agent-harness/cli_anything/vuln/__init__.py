import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vuln running')
@cli.command()
def start(): click.echo('vuln started')
if __name__ == '__main__': cli()
