import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('NPM status: running')
@cli.command()
@click.argument('domain')
def proxy(domain): click.echo(f'Proxy: {domain}')
if __name__ == '__main__': cli()
