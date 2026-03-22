import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def dir(url): subprocess.run(['gobuster', 'dir', '-u', url, '-w', '/usr/share/wordlists/dirb/common.txt'])
@cli.command()
@click.argument('domain')
def dns(domain): subprocess.run(['gobuster', 'dns', '-d', domain])
if __name__ == '__main__': cli()
