import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def stats(): click.echo('HAProxy stats on :8404/stats')
@cli.command()
def status(): click.echo('HAProxy running')
if __name__ == '__main__': cli()
